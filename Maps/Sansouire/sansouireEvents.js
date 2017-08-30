let events = []
let condition = function(name, cond) {
    this.name = name
    // this.func = (prop) => {
    //     if (cond) {return true}return false
    // }
    this.func = cond
}

let toMap = [
    [
        "snow", {  // Snow: sunshine -60 water +10, if temperature < 0 and it's winter
            "sunshine": -60,
            "water": +10
        },
        [
            new condition("temperature", p => p < 0), 
            new condition("season", p => p == "winter")]
        ],
    [
        "mosquito_eradication",  // Mosquito_eradication: no effect on field, just on plants
        // there is no effect, condition: spring
        {}, // Plants are suppose to handle this as a global growing decrease (except for obione)
        [new condition("season", p => p == "spring")]

    ],
    [
        "storm",
        {
            "salinity": -20,
            "water": +40
        },
        [new condition("temperature", p => p > 25)]
    ],
    [
        "heat_wave",
        {
            "sunshine": +60,
            "salinity": -20,
            "water": +40
        },
        [new condition("temerature"), p => p > 35]
    ]
]

for (map of toMap) {
    events.push(new Event(map[0], map[1], map[2]))
}