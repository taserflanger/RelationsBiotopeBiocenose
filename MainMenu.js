Game.MainMenu = function(game) {

}

let Button

Game.MainMenu.prototype = {
    create: function() {
        this.stage.backgroundColor = '#3A5964'
        this.Play = function() {
            this.state.start('MapSansouire')
        }
        this.Play = this.Play.bind(this)
        button = this.add.button(this.world.centerX, this.world.centerY - 150, 'buttons',this.Play, this, 1, 0, 2)
    },
    update: function() {
        if (debug) {
            this.Play()
        }
    }
}