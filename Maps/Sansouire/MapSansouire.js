Game.MapSansouire = function(game) {
    
}

let field = new Field("Sansouire", {
    "surface": 100, 
    "temperature": -    10, 
    "water": 100, 
    "sunshine": 100,
    "season": "winter"})
let plant1 = new Plant("Salicorne", {
    "sun": 0,
    "cold_resistance": 1, 
    "hot_resistance": 1,
    "salty_ground": 2, 
    "other": {"salt_extraction": false, "viral_resistance": false, "supports_trampling": true}
})
let plant2 = new Plant("Soude", {
    "sun": -1,
    "cold_resistance": -1,
    "hot_resistance": 0.5,
    "salty_ground": -1,
    "other": {"salt_extraction": true, "viral_resistance": false, "supports_trampling": true}
})

// events array is defined in the corresponding Events File ad global scope
// The corresponding file has to load before this one
field.applyEvent(events[0])
console.log(field.properties.sunshine)

Game.MapSansouire.prototype = {
    
    create:function() {
        this.stage.backgroundColor = '#e9ffe8'
        let map = this.add.sprite(0, 0, 'SansouireField')
    },
    update: function() {}

}