Game.MainMenu = function(game) {

}

let Button

Game.MainMenu.prototype = {
    create: function() {
        this.stage.backgroundColor = '#3A5964'
        this.Play = function() {
            this.state.start('MapSansouire') // There is still no map menu, because there is 
                                             // only one map
        }
        this.Play = this.Play.bind(this) // use the this.state inside the play function
        button = this.add.button(this.world.centerX, this.world.centerY - 150, 'buttons',this.Play, this, 1, 0, 2)
    },
    update: function() {
        // Skip the mainMenu if debug mode enabled in index.js
        if (debug) {
            this.Play()
        }
    }
}