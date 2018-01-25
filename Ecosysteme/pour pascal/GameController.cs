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
	public GameObject mapPropertiesDisplay;
	public SeasonDisplay seasonDisplay;
	public float episodeTransitionLength;
	public int averageEpisodeLength;
	public int averageWeatherLength;

	public Properties mapProperties;
	public Player[] players;

	public Light directionalLight;
	Season season;
	Weather weather;
	Episode episode;
	Episode nextEpisode;
	float weatherLength;
	float episodeLength;
	public Text episodeDisplay;
	public Text nextEpisodeDisplay;
	public Text weatherDisplay;
	public System.Random rnd;
	public Dictionary<string, float[]> episodeAimRange;
	public float drivenSpawnFactor;
	Dictionary<string, float> episodeAim;
	HexGrid grid;
	float lightIntensityAim;
	Color lightColorAim;

	void Awake() {
		grid = GetComponentInChildren<HexGrid> ();
		grid.transform.SetParent (transform);
		mapProperties = new Properties ();
		season = Season.winter;
		weather = Weather.sunny;
		nextEpisode = Episode.fog;
		rnd = new System.Random ();
		ChooseNextEpisode ();
		episodeDisplay.text = episode.ToString ();
		nextEpisodeDisplay.text = nextEpisode.ToString ();
		nextEpisodeDisplay.rectTransform.localPosition = new Vector3 (200f, 0f, 0f);
		nextEpisodeDisplay.color = new Color (0.196f, 0.196f, 0.196f, 0f);
		weatherDisplay.text = weather.ToString ();
		episodeLength = rnd.Next (averageEpisodeLength - ((int)averageEpisodeLength/4), averageEpisodeLength + ((int)averageEpisodeLength/4));
		weatherLength = rnd.Next (averageWeatherLength - ((int)averageWeatherLength/4), averageWeatherLength + ((int)averageWeatherLength/4));
		episodeAimRange = new Dictionary<string, float[]> ();
		episodeAim = new Dictionary<string, float> ();
		drivenSpawnFactor = 1;
		UpdateLightAim ();
		UpdateDisplay ();

	}

	void OnEnable() {
		seasonDisplay.SetImage (0);
	}

	void Start() {
		SetEpisodeAimRange ();
		GetEpisodeAim ();
		StartCoroutine (ChangeValue ());
		StartCoroutine (MetaSeasonCoroutine ());
		StartCoroutine (MetaEpisodeCoroutine ());
		StartCoroutine (MetaWeatherCoroutine ());
	}
	void Update() {
		directionalLight.transform.RotateAround (directionalLight.transform.position, new Vector3 (0f, 1f, 0f), .06f);
		for (int i = 0; i < players.Length; i++) {
			players [i].updateParams ();
		}
		grid.UpdateCellsProbas (players);
		if ((int)(Time.time * 20) % 10 == 0) {
			//grid.UpdatePlayersCells (players);
		}


		UpdateDisplay ();
	}

	IEnumerator MetaSeasonCoroutine() {
		StartCoroutine (DisplayFade (300f, 0f));
		while (true) {
			yield return new WaitForSeconds((float)GameVariables.SeasonLength);
			StartCoroutine (SeasonCoroutine ());
		}
	}

	IEnumerator MetaEpisodeCoroutine() {
		while (true) {
			yield return new WaitForSeconds ((float)episodeLength);
			StartCoroutine (EpisodeCoroutine ());
		}
	}

	IEnumerator MetaWeatherCoroutine() {
		while (true) {
			yield return new WaitForSeconds ((float)weatherLength);
			StartCoroutine (WeatherCoroutine ());
		}
	}

	IEnumerator SeasonCoroutine() {
		season = season.Next ();
		UpdateLightAim ();
		seasonDisplay.SetImage ((int)season);
		yield return null;
	}

	IEnumerator EpisodeCoroutine() {
		episodeLength = rnd.Next (averageEpisodeLength - ((int)averageEpisodeLength/4), averageEpisodeLength + ((int)averageEpisodeLength/4));
		nextEpisodeDisplay.text = nextEpisode.ToString ();
		StartCoroutine (DisplayFade (200f, 0f));
		SetEpisodeAimRange ();
		GetEpisodeAim ();
		StartCoroutine (ChangeValue ());
		episodeDisplay.text = episode.ToString ();
		yield return null;
	}

	IEnumerator DisplayFade (float begin, float end) {
		while (Mathf.Abs (nextEpisodeDisplay.rectTransform.localPosition.x - end) >= 0.05) {
			float newPos = Mathf.Lerp (nextEpisodeDisplay.rectTransform.localPosition.x, end, Time.deltaTime);
			nextEpisodeDisplay.rectTransform.localPosition = new Vector3 (newPos, 0f, 0f);
			float alpha = Mathf.Lerp (nextEpisodeDisplay.color.a, 1f, Time.deltaTime);
			var tempColor = nextEpisodeDisplay.color;
			tempColor.a = alpha;
			nextEpisodeDisplay.color = tempColor;
			alpha = Mathf.Lerp (episodeDisplay.color.a, 0f, Time.deltaTime);
			tempColor = episodeDisplay.color;
			tempColor.a = alpha;
			episodeDisplay.color = tempColor;
			yield return null;
		}
		episode = nextEpisode;
		episodeDisplay.text = episode.ToString ();
		episodeDisplay.color = new Color (0.196f, 0.196f, 0.196f, 1f); 
		nextEpisodeDisplay.color = new Color (0.196f, 0.196f, 0.196f, 0f);
		nextEpisodeDisplay.rectTransform.localPosition = new Vector3 (200f, 0f, 0f);
		ChooseNextEpisode ();
	}

	IEnumerator WeatherCoroutine() {
		weatherLength = rnd.Next ((int)averageWeatherLength - ((int)averageWeatherLength/4), averageWeatherLength + ((int)averageWeatherLength/4));
		weather = (Weather)Random.Range (0, 3);
		Debug.Log (weather);
		weatherDisplay.text = weather.ToString ();
		yield return null;
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
		episodeAimRange.Clear ();
		if (episode == Episode.mosquito) {
			episodeAimRange.Add ("Growing", new float[]{ 0.5f, 0.7f });
			} 
		else if (episode == Episode.none){
			if (weather = Weather.rainy){
				episodeAimRange.Add ("Water", new float[] { 0.5f, 0.9f})
			}
			if (weather == Weather.sunny){
				episodeAimRange.Add ("Sunshine", new float[] {0.6f, 0.9f})
			}
			if (weather == Weather.windy){
				episodeAimRange.Add ("Temperature", new float[] {current_temperature - 0.1f})
			}
			if (weather == Weather.cloudy){
				episodeAimRange.Add ("Sunshine", new float[] {0.3, 0.6})
			}
		}
		else if (episode == Episode.orage) {
			if (season == Season.winter) {
				episodeAimRange.Add ("Sunshine", new float[] { 0.0f, 0.05f });
				episodeAimRange.Add ("Water", new float[] { 0.5f, 0.9f });
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
				episodeAimRange.Add ("Salinity", new float[] { 0.2f, 0.3f });
			}
		} else if (episode == Episode.sun_heat) {
			episodeAimRange.Add ("Sunshine", new float[] { 0.8f, 1.0f });
			float current_water = mapProperties.Values [1];
			episodeAimRange.Add ("Water", new float[] { current_water 0.3f, current_water 0.1f });

		} else if (episode == Episode.overflowing) {
			episodeAimRange.Add ("Sunshine", new float[] { 0.2f, 0.4f });
			episodeAimRange.Add ("Water", new float[] { 0.8f, 0.9f });

		} else if (episode == Episode.gathering) {
			float current_sunshine = mapProperties.Values [2];
			episodeAimRange.Add ("Sunshine", new float[] { current_sunshine + 0.1f, current_sunshine + 0.2f });
			episodeAimRange.Add ("Growing", new float[] { 0.8f, 0.9f });

		} else if (episode == Episode.trampling) {
			//In this event, salicorne, has a lower growing
			episodeAimRange.Add ("Sunshine", new float[] { 0.5f, 0.8f });

		} else if (episode == Episode.pollution) {
			episodeAimRange.Add ("Growing", new float[] { 0.3f, 0.6f });

		} else if (episode == Episode.fog) {
			if (season == winter) {
				episodeAimRange.Add ("Water", new float[] { current_water + 0.2f, current_water + 0.3f });}
			else if (season == spring) {
				episodeAimRange.Add ("Water", new float[] { current_water + 0.2f, current_water + 0.3f });
			}
			else if (season == summer) {
				episodeAimRange.Add ("Water", new float[] { 0.5f, 0.8f });
			}
			else if (season == automn) {
				episodeAimRange.Add ("water", new float[] { current_water + 0.3})
			}
			float current_sun = mapProperties.Values [2];
			episodeAimRange.Add ("Sunshine", new float[] { current_sunshine - 0.3f, current_sun - 0.2f });
		}
		else if (episode == Episode.northern_wind) {
			episodeAimRange.Add ("Sunshine", new float[] { 0.7f, 0.9f });
			episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.6f})
		}
		else if (episode == Episode.southern_wind) {
			episodeAimRange.Add ("Sunshine", new float[] { 0.4f, 0.6f });
			episodeAimRange.Add ("Salinity", new float[] { 0.6f, 0.8f})
		}
		else if (episode == Episode.snow) {
			episodeAimRange.Add ("Sunshine", new float[] { 0.5f, 0.6f})
			episodeAimRange.Add ("Water", new float[] {current_water + 0.1f})
			episodeAimRange.Add ("Temperature", new float[] {0f, 0.12f})
		}
		else if(episode == Episode.storm_northern_wind){
			episodeAimRange.Add ("Sunshine", new float[] { 0.8f, 1.0f });
			episodeAimRange.Add ("Salinity", new float[] { 0.3f, 0.6f})
		}
		else if(episode == Episode.storm_southern_wind){
			episodeAimRange.Add ("Sunshine", new float[] { 0.2f, 0.5f });
			episodeAimRange.Add ("Salinity", new float[] { 0.7f, 0.9f})

			}

		foreach (KeyValuePair<string, float[]> keyValuePair in episodeAimRange) {
			float[] value = keyValuePair.Value;
			for (int i = 0; i < value.Length; i++) {
				if (value [i] > 1) {
					value[i] = 1;
				} else if (value [i] < 0) {
					value[i] = 0;
				}
			}
		}
	}
		
	void ChooseNextEpisode() {
		float[] probabilities = new float[EpisodeExtensions.Length];
		if (season == Season.winter) {
			if (weather == Weather.rainy){
				probabilities [(int)Episode.orage] = 20f;
				probabilities [(int)Episode.none] = 50f;
				probabilities[(int)Episode.snow] = 10f
				probabilities[(int)Episode.pollution] = 15f 
				probabilities [(int)Episode.southern_wind] = 40f;
				probabilities [(int)Episode.storm_southern_wind] = 25f

			}
			
			else if (weather == Weather.sunny){
				probabilities [(int)Episode.none] = 50f;
				probabilities [(int)Episode.northern_wind] = 45f;
				probabilities [(int)Episode.storm_northern_wind] = 20f
				probabilities [(int)Episode.trampling] = 30f
			}

			else if (weather == Weather.cloudy){
				probabilities [(int)Episode.none] = 50f;
				probabilities [(int)Episode.fog] = 30f;
				probabilities [(int)Episode.storm_southern_wind] = 25f
				probabilities [(int)Episode.trampling] = 25f

			}

		} else if (season == Season.spring) {
			if (weather == Weather.rainy){
				probabilities [(int)Episode.none] = 50f;
				probabilities [(int)Episode.northern_wind]= 55f

			}
			else if (weather == Weather.sunny){
				probabilities [(int)Episode.none] = 50f;
				probabilities [(int)Episode.mosquito] = 10f

			}
			else if (weather == Weather.cloudy){
				probabilities [(int)Episode.none] = 50f;
				probabilities [(int)Episode.fog] = 30f;
				probabilities [(int)Episode.southern_wind]=45f
			
			}

			probabilities [(int)Episode.mosquito] = 30f;
			probabilities [(int)Episode.orage] = 40f;
			probabilities [(int)Episode.gathering] = 40f;
			probabilities [(int)Episode.pollution] = 10f;
		} else if (season == Season.summer) {
			probabilities [(int)Episode.sun_heat] = 50f;
			probabilities [(int)Episode.pollution] = 20f;
		} else if (season == Season.automn) {
			probabilities [(int)Episode.overflowing] = 40f;
			probabilities [(int)Episode.pollution] = 30f;
		}
		else if (weather == rainy){
			probabilities [(int)]
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
		Slider[] sliders = mapPropertiesDisplay.GetComponentsInChildren<Slider> ();
		for (int i = 0; i < mapProperties.Length; i++) {
			sliders [i].value = mapProperties.Values [i];
		}
		sliders [3].value = drivenSpawnFactor;
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

