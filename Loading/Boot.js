let Game = {}

Game.Boot = function(game) {}

Game.Boot.prototype = {
    init:function() {
        this.input.MaxPointers = 2 // 2 player game = 2 pointers on screen
        this.stage.disableVisibilityChange = false // Game Pauses when screen left
    },
    preload: function() {
        this.load.image('phaserImage', './assets/preloader.png')
    },
    create: function() {
        this.state.start('Preloader')
    }
}