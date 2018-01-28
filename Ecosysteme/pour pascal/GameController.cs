using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Linq;

public class GameController : MonoBehaviour {

	public Episode GameEpisode {
		get {
			return episode;
		}
	}

	public Episode GameNextEpisode {
		get {
			return nextEpisode;
		}
	}

	public Weather GameWeather {
		get{
			return weather;
		}
	}

	public Season GameSeason {
		get {
			return season;
		}
	}

	public HexGrid gridPrefab;
	public int playerCount = 2;
	public int beginningSize = 2;

	public float episodeTransitionLength;
	public int averageEpisodeLength;
	public int averageWeatherLength;
	public UIController uiController;

	public Properties mapProperties;
	public Player[] players;

	public Light directionalLight;
	Season season;
	Weather weather;
	Weather nextWeather;
	Episode episode;
	Episode nextEpisode;
	float weatherLength;
	float episodeLength;

	public System.Random rnd;
	public Dictionary<string, float[]> episodeAimRange;
	public float drivenSpawnFactor;
	Dictionary<string, float> episodeAim;
	HexGrid grid;
	float lightIntensityAim;
	Color lightColorAim;
	int episodeCount;
	int weatherCount;

	void Awake() {
		grid = GetComponentInChildren<HexGrid> ();
		grid.transform.SetParent (transform);
		mapProperties = new Properties ();
		season = Season.winter;
		weather = Weather.sunny;
		nextEpisode = Episode.fog;
		rnd = new System.Random ();
		ChooseNextEpisode ();
		uiController.episodeDisplay.SetSprite((int)episode);
		uiController.episodeDisplay.SetNextSprite((int)nextEpisode);
		uiController.episodeDisplay.activeImage.color = new Color (1f, 1f, 1f, 0f);
		uiController.episodeDisplay.nextImage.color = new Color (1f, 1f, 1f, 0f);
		uiController.weatherDisplay.activeImage.color = new Color (1f, 1f, 1f, 0f);
		uiController.weatherDisplay.nextImage.color = new Color (1f, 1f, 1f, 0f);
		ChooseNextWeather();
		uiController.weatherDisplay.nextTransform.localPosition = new Vector3 (-200f, 0f, 0f);
		uiController.weatherDisplay.SetNextSprite ((int)nextWeather);
		episodeLength = rnd.Next (averageEpisodeLength - ((int)averageEpisodeLength/4), averageEpisodeLength + ((int)averageEpisodeLength/4));
		weatherLength = rnd.Next (averageWeatherLength - ((int)averageWeatherLength/4), averageWeatherLength + ((int)averageWeatherLength/4));
		episodeAimRange = new Dictionary<string, float[]> ();
		episodeAim = new Dictionary<string, float> ();
		drivenSpawnFactor = 1;
		UpdateLightAim ();
		UpdateDisplay ();
		SetEpisodeAimRange ();
		GetEpisodeAim ();
	}

	void OnEnable() {
		uiController.seasonDisplay.SetImage (0);
	}

	void Start() {
		uiController.weatherDisplay.FadeIn ();
		uiController.episodeDisplay.FadeIn ();
		StartCoroutine (ChangeValue ());
		StartCoroutine (MetaSeasonCoroutine ());
		StartCoroutine (MetaEpisodeCoroutine ());
		StartCoroutine (MetaWeatherCoroutine ());
		uiController.SetText ("beginning");
	}

	void Update() {
		if (Time.timeScale > 0) {
			directionalLight.transform.RotateAround (directionalLight.transform.position, new Vector3 (0f, 1f, 0f), Time.deltaTime);
			for (int i = 0; i < players.Length; i++) {
				players [i].updateParams ();
				players [i].SetGlobalGrowingCroissance (grid.GetCell (new HexCoordinates (0, 0)));
			}
			grid.UpdateCellsProbas (players);
			//if ((int)(Time.time * 10) % 30 == 0) {
			grid.UpdatePlayersCells (players);
			//}
			UpdateDisplay ();
		}
	}

	IEnumerator MetaSeasonCoroutine() {
		while (true) {
			yield return new WaitForSeconds((float)GameVariables.SeasonLength);
			StartCoroutine (SeasonCoroutine ());
		}
	}

	IEnumerator MetaEpisodeCoroutine() {
		while (true) {
			yield return new WaitForSeconds ((float)episodeLength);
			episodeCount++;
			StartCoroutine (EpisodeCoroutine ());
		}
	}

	IEnumerator MetaWeatherCoroutine() {
		while (true) {
			yield return new WaitForSeconds ((float)weatherLength);
			StartCoroutine (WeatherCoroutine ());
			weatherCount++;
		}
	}

	IEnumerator SeasonCoroutine() {
		season = season.Next ();
		UpdateLightAim ();
		uiController.seasonDisplay.SetImage ((int)season);
		yield return null;
	}

	IEnumerator EpisodeCoroutine() {
		if (episodeCount == 1) {
			uiController.SetText ("firstEpisode");
		}
		if (episodeCount == 2) {
			//uiController.SetText ("");
		}
		episodeLength = rnd.Next (averageEpisodeLength - ((int)averageEpisodeLength/4), averageEpisodeLength + ((int)averageEpisodeLength/4));
		//uiController.episodeDisplay.SetNextSprite ((int)nextEpisode);
		uiController.StartCoroutine (DisplayFadeEpisode(200f, 0f, uiController.episodeDisplay));
		SetEpisodeAimRange ();
		GetEpisodeAim ();
		StartCoroutine (ChangeValue ());
		//uiController.episodeDisplay.SetSprite ((int)episode);
		yield return null;
	}

	IEnumerator WeatherCoroutine() {
		weatherLength = rnd.Next ((int)averageWeatherLength - ((int)averageWeatherLength/4), averageWeatherLength + ((int)averageWeatherLength/4));
		//uiController.weatherDisplay.SetNextSprite ((int)nextWeather);
		StartCoroutine (DisplayFadeWeather (-200f, 0f, uiController.weatherDisplay));
		//uiController.weatherDisplay.SetSprite ((int)weather);
		yield return null;
	}

	public IEnumerator DisplayFadeEpisode (float begin, float end, LogoDisplay display) {
		while (Mathf.Abs (display.nextTransform.localPosition.x - end) >= 0.05) {
			float newPos = Mathf.Lerp (display.nextTransform.localPosition.x, end, Time.deltaTime);
			display.nextTransform.localPosition = new Vector3 (newPos, 0f, 0f);
			float alpha = Mathf.Lerp (display.nextImage.color.a, 1f, Time.deltaTime);
			var tempColor = display.nextImage.color;
			tempColor.a = alpha;
			display.nextImage.color = tempColor;
			alpha = Mathf.Lerp (display.activeImage.color.a, 0f, Time.deltaTime);
			tempColor = display.activeImage.color;
			tempColor.a = alpha;
			display.activeImage.color = tempColor;
			yield return null;
		}
		episode = nextEpisode;
		ChooseNextEpisode ();
		display.SetSprite((int)episode);
		display.SetNextSprite ((int)nextEpisode);
		display.activeImage.color = new Color (1f, 1f, 1f, 1f); 
		display.nextImage.color = new Color (1f, 1f, 1f, 0f);
		display.nextTransform.localPosition = new Vector3 (begin, 0f, 0f);
	}

	public IEnumerator DisplayFadeWeather (float begin, float end, LogoDisplay display) {
		while (Mathf.Abs (display.nextTransform.localPosition.x - end) >= 0.05) {
			float newPos = Mathf.Lerp (display.nextTransform.localPosition.x, end, Time.deltaTime);
			display.nextTransform.localPosition = new Vector3 (newPos, 0f, 0f);
			float alpha = Mathf.Lerp (display.nextImage.color.a, 1f, Time.deltaTime);
			var tempColor = display.nextImage.color;
			tempColor.a = alpha;
			display.nextImage.color = tempColor;
			alpha = Mathf.Lerp (display.activeImage.color.a, 0f, Time.deltaTime);
			tempColor = display.activeImage.color;
			tempColor.a = alpha;
			display.activeImage.color = tempColor;
			yield return null;
		}
		weather = nextWeather;
		ChooseNextWeather ();
		display.SetSprite((int)weather);
		display.SetNextSprite ((int)nextWeather);
		display.activeImage.color = new Color (1f, 1f, 1f, 1f); 
		display.nextImage.color = new Color (1f, 1f, 1f, 0f);
		display.nextTransform.localPosition = new Vector3 (begin, 0f, 0f);
	}


	void ChooseNextWeather () {
		float[] probabilities = new float[WeatherExtensions.Length];
		if (season == Season.winter) {
			probabilities [(int)Weather.cloudy] = 3f;
			probabilities [(int)Weather.rainy] = 1f;
			probabilities [(int)Weather.sunny] = 2f;
		} else if (season == Season.spring) {
			probabilities [(int)Weather.cloudy] = 2f;
			probabilities [(int)Weather.rainy] = 2f;
			probabilities [(int)Weather.sunny] = 3f;
		} else if (season == Season.summer) {
			probabilities [(int)Weather.cloudy] = 2f;
			probabilities [(int)Weather.rainy] = 1f;
			probabilities [(int)Weather.sunny] = 4f;
		} else if (season == Season.automn) {
			probabilities [(int)Weather.cloudy] = 2f;
			probabilities [(int)Weather.rainy] = 3f;
			probabilities [(int)Weather.sunny] = 2f;
		}
		List<float> probList = probabilities.ToList ();
		float summation = probList.Sum ();
		float random_n = rnd.Next (1, (int)summation);
		int index = int.MaxValue;
		for (int i = 0; i < probabilities.Length; i++) {
			random_n -= probabilities [i];
			if (random_n < 0) {
				index = i;
				break;
			}
		}
		nextWeather = (Weather)index;
	}

	void UpdateLightAim() {
		if (season == Season.winter) {
			lightIntensityAim = 0.6f;
			lightColorAim = new Color (0.78f, 0.866f, 0.886f);
		} else if (season == Season.spring) {
			lightIntensityAim = 1f;
			lightColorAim = new Color (1f, 0.95f, 0.83f);
		} else if (season == Season.summer) {
			lightIntensityAim = 1.3f;
			lightColorAim = new Color (1f, 1f, 0.71f);
		} else if (season == Season.automn) {
			lightIntensityAim = 0.8f;
			lightColorAim = new Color (0.91f, 0.81f, 0.77f);
		}
	}

	void GetEpisodeAim() {
		foreach (KeyValuePair<string, float[]> keyValue in episodeAimRange) {
			string key = keyValue.Key;
			float[] valueRange = keyValue.Value;
			float value = rnd.Next ((int)(valueRange[0] * 100), (int)(valueRange[1] * 100)) / 100f;
			episodeAim [key] = value;
		}
	}

	void SetEpisodeAimRange() {
		float current_salinity = mapProperties.Values [0];
		// la salinité ne descend pas en dessous de 0.5 en été
		float current_water = mapProperties.Values [1];
		float current_sunshine = mapProperties.Values [2];
		float current_temperature = mapProperties.Values [3];

		episodeAimRange.Clear ();
		if (episode == Episode.mosquito) {
			episodeAimRange.Add ("Growing", new float[]{ 0.5f, 0.7f });
		} else if (episode == Episode.none) {
			episodeAimRange.Add ("Growing", new float[] { 1f, 1f });
			if (weather == Weather.rainy) {
				episodeAimRange.Add ("Water", new float[] { 0.5f, 0.9f });
				if (season == Season.winter) {
					episodeAimRange.Add ("Temperature", new float[] { 0.1f, 0.2f });
				} else if (season == Season.spring) {
					episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
				} else if (season == Season.summer) {
					episodeAimRange.Add ("Temperature", new float[] { 0.6f, 0.85f });
					episodeAimRange.Add ("Salinity", new float[] { 0.75f, 0.85f });
				} else if (season == Season.automn) {
					episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
					episodeAimRange.Add ("Salinity", new float[] { 0.4f, 0.7f });
				}
			}
			if (weather == Weather.sunny) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.6f, 0.9f });
				if (season == Season.winter) {
					episodeAimRange.Add ("Temperature", new float[] { 0.2f, 0.25f });
				} else if (season == Season.spring) {
					episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
					episodeAimRange.Add ("Salinity", new float[] { 0.4f, 0.7f });
				} else if (season == Season.summer) {
					episodeAimRange.Add ("Temperature", new float[] { 0.75f, 0.9f });
					episodeAimRange.Add ("Salinity", new float[] { 0.7f, 0.9f });
				} else if (season == Season.automn) {
					episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
					episodeAimRange.Add ("Salinity", new float[] { 0.4f, 0.7f });
				}

			}			
			if (weather == Weather.cloudy) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.3f, 0.6f });
				if (season == Season.winter) {
					episodeAimRange.Add ("Temperature", new float[] { 0.1f, 0.2f });
				} else if (season == Season.spring) {
					episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.55f });
				} else if (season == Season.summer) {
					episodeAimRange.Add ("Temperature", new float[] { 0.6f, 0.85f });
					episodeAimRange.Add ("Salinity", new float[] { 0.7f, 0.9f });
				} else if (season == Season.automn) {
					episodeAimRange.Add ("Temperature", new float[] { 0.25f, 0.5f });
				}
			}
		} else if (episode == Episode.orage) {
			episodeAimRange.Add ("Growing", new float[] { 1f, 1f });
			if (season == Season.winter) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.0f, 0.05f });
				episodeAimRange.Add ("Water", new float[] { 0.5f, 0.9f });
				episodeAimRange.Add ("Temperature", new float[] { 0.1f, 0.25f });
				episodeAimRange.Add ("Salinity", new float[] { 0.2f, 0.5f });
				//Debug.Log ("Snow Storm");
			} else if (season == Season.automn) {
				episodeAimRange.Add ("Sushine", new float[] { 0.0f, 0.1f });
				episodeAimRange.Add ("Water", new float[] { 0.6f, 0.9f });
				episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.4f });
			} else if (season == Season.spring) {
				episodeAimRange.Add ("Sushine", new float[] { 0.0f, 0.1f });
				episodeAimRange.Add ("Water", new float[] { 0.6f, 0.9f });
				episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.4f });
			} else if (season == Season.summer) {
				episodeAimRange.Add ("Sushine", new float[] { 0.0f, 0.1f });
				episodeAimRange.Add ("Water", new float[] { 0.6f, 0.9f });
				episodeAimRange.Add ("Salinity", new float[] { 0.5f, 0.6f });
				episodeAimRange.Add ("Temperature", new float[] { 0.65f, 0.8f });

			}
		} else if (episode == Episode.sun_heat) {
			// événement extrème
			episodeAimRange.Add ("Sunshine", new float[] { 0.8f, 1.2f });
			episodeAimRange.Add ("Water", new float[] { -0.2f, 0.2f });
			episodeAimRange.Add ("Temperature", new float[] { 0.95f, 1.1f });
			episodeAimRange.Add ("Growing", new float[] { 0.7f, 0.9f });

		} else if (episode == Episode.overflowing) {
			episodeAimRange.Add ("Sunshine", new float[] { 0.2f, 0.4f });
			episodeAimRange.Add ("Water", new float[] { 0.8f, 0.9f });

		} else if (episode == Episode.gathering) {
			if (season == Season.summer) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.8f, 0.9f });
				episodeAimRange.Add ("Growing", new float[] { 0.8f, 0.9f });
			} else {
				episodeAimRange.Add ("Sunshine", new float[] { current_sunshine + 0.1f, current_sunshine + 0.2f });
				episodeAimRange.Add ("Growing", new float[] { 0.8f, 0.9f });
			}

		} else if (episode == Episode.trampling) {
			//In this event, salicorne, has a lower growing
			episodeAimRange.Add ("Sunshine", new float[] { 0.5f, 0.8f });
			episodeAimRange.Add ("Growing", new float[] { 0.7f, 0.9f });


		} else if (episode == Episode.pollution) {
			episodeAimRange.Add ("Growing", new float[] { 0.3f, 0.6f });

		} else if (episode == Episode.fog) {
			episodeAimRange.Add ("Growing", new float[] { 1f, 1f });
			if (season == Season.winter) {
				episodeAimRange.Add ("Water", new float[] { current_water + 0.2f, current_water + 0.3f });
			} else if (season == Season.spring) {
				episodeAimRange.Add ("Water", new float[] { current_water + 0.2f, current_water + 0.3f });
			} else if (season == Season.summer) {
				episodeAimRange.Add ("Water", new float[] { 0.5f, 0.8f });
			} else if (season == Season.automn) {
				episodeAimRange.Add ("water", new float[] { current_water + 0.3f, current_water +0.3f });
			}
			episodeAimRange.Add ("Sunshine", new float[] { current_sunshine - 0.3f, current_sunshine - 0.2f });
		} else if (episode == Episode.northern_wind) {
			episodeAimRange.Add ("Growing", new float[] { 1f, 1f });
			episodeAimRange.Add ("Sunshine", new float[] { 0.7f, 0.9f });
			if (season == Season.winter) {
				episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.6f });
				episodeAimRange.Add ("Temperature", new float[] { 0.1f, 0.25f });
			} else if (season == Season.spring) {
				episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
				episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.6f });
			} else if (season == Season.summer) {
				episodeAimRange.Add ("Temperature", new float[] { 0.8f, 0.9f });
				episodeAimRange.Add ("Salinity", new float[] { 0.5f, 0.7f });
			} else if (season == Season.automn) {
				episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
				episodeAimRange.Add ("Salinity", new float[] { 0.4f, 0.6f});
			}
		} else if (episode == Episode.southern_wind) {
			episodeAimRange.Add ("Growing", new float[] { 1f, 1f });
			episodeAimRange.Add ("Sunshine", new float[] { 0.4f, 0.6f });
			episodeAimRange.Add ("Salinity", new float[] { 0.6f, 0.8f });
			if (season == Season.winter) {
				episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.6f });
				episodeAimRange.Add ("Temperature", new float[] { 0.05f, 0.25f });
			} else if (season == Season.spring) {
				episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
				episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.6f });
			} else if (season == Season.summer) {
				episodeAimRange.Add ("Temperature", new float[] { 0.8f, 0.9f });
				episodeAimRange.Add ("Salinity", new float[] { 0.5f, 0.7f });
			} else if (season == Season.automn) {
				episodeAimRange.Add ("Temperature", new float[] { 0.3f, 0.6f });
				episodeAimRange.Add ("Salinity", new float[] { 0.4f, 0.6f });
			} else if (episode == Episode.snow) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.5f, 0.6f });
				episodeAimRange.Add ("Water", new float[] { current_water + 0.1f, current_water + 0.1f });
				episodeAimRange.Add ("Temperature", new float[] { 0f, 0.12f });
				episodeAimRange.Add ("Growing", new float[] { 0.8f, 0.9f });

			} else if (episode == Episode.storm_northern_wind) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.8f, 1.0f });
				episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.6f });
			} else if (episode == Episode.storm_southern_wind) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.2f, 0.5f });
				episodeAimRange.Add ("Salinity", new float[] { 0.7f, 0.9f });

			}
		}

		foreach (KeyValuePair<string, float[]> keyValuePair in episodeAimRange) {
			float[] value = keyValuePair.Value;
			for (int i = 0; i < value.Length; i++) {
				if (value [i] > 1) {
					value [i] = 1;
				} else if (value [i] < 0) {
					value [i] = 0;
				}
			}
		}
	}
		
	void ChooseNextEpisode() {
		float[] probabilities = new float[EpisodeExtensions.Length];
		if (season == Season.winter) {
			probabilities [(int)Episode.orage] = 50f;
			probabilities [(int)Episode.southern_wind] = 40f;
			probabilities [(int)Episode.northern_wind] = 45f;
			probabilities [(int)Episode.fog] = 30f;
		} else if (season == Season.spring) {
			probabilities [(int)Episode.mosquito] = 30f;
			probabilities [(int)Episode.orage] = 50f;
			probabilities [(int)Episode.gathering] = 40f;
		} else if (season == Season.summer) {
			probabilities [(int)Episode.sun_heat] = 50f;
		} else if (season == Season.automn) {
			probabilities [(int)Episode.overflowing] = 40f;
}
		List<float> probList = probabilities.ToList ();
		float summation = probList.Sum ();
		float random_n = rnd.Next (1, (int)summation);
		int index = int.MaxValue;
		for (int i = 0; i < probabilities.Length; i++) {
			random_n -= probabilities [i];
			if (random_n < 0) {
				index = i;
				break;
			}
		}

		nextEpisode = (Episode)index;
	}

	void UpdateDisplay() {
		Slider[] sliders = uiController.mapPropertiesDisplay.GetComponentsInChildren<Slider> ();
		for (int i = 0; i < mapProperties.Length; i++) {
			sliders [i].value = mapProperties.Values [i];
		}
		sliders [4].value = drivenSpawnFactor;
	}

	IEnumerator ChangeValue() {
		for (int i = 0; i < mapProperties.Length; i++) {
			float endValue = float.MinValue;
			bool mapChange = true;
			bool exists = true;
			try {
				endValue = episodeAim [mapProperties.Keys [i]];
			} catch {
				if (episodeAim.Keys.Contains ("Growing")) {
					endValue = episodeAim ["Growing"];
					mapChange = false;
				} else {
					exists = false;
				}
			}
			if (mapChange && exists) {
				while (Mathf.Abs (mapProperties.Values [i] - endValue) >= 0.05) {
					mapProperties.SetProperty (i, Mathf.Lerp (mapProperties.Values [i], endValue, Time.deltaTime/episodeTransitionLength));
					drivenSpawnFactor = Mathf.Lerp (drivenSpawnFactor, 1f, Time.deltaTime/episodeTransitionLength);
					yield return null;
				}
			} else if (exists) {
				while (Mathf.Abs (drivenSpawnFactor - endValue) >= 0.05) {
					drivenSpawnFactor = Mathf.Lerp (drivenSpawnFactor, endValue, Time.deltaTime/episodeTransitionLength);
					yield return null;
				}
			} else {
				yield return null;
			}
		}
	}
		
}

public static class IEnumerableExtensions {
	public static IEnumerable<float> CumulativeSum(this IEnumerable<float> sequence)
	{
		float sum = 0;
		foreach(var item in sequence)
		{
			sum += item;
			yield return sum;
		}        
	}

}

