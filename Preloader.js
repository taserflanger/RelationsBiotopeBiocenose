Game.Preloader = function(game) {
    // reference to preload images
}

Game.Preloader.prototype = {
    preload: function() {
        
        // Load all assets
        this.load.spritesheet('buttons', './assets/buttons.png', 208, 59)
        this.load.image('SansouireField', 'assets/MapSansouire.png')
    },
    create: function() {
        this.phaserImage = this.add.sprite(this.world.centerX,
            this.world.centerY, 
            'phaserImage')

        this.phaserImage.anchor.setTo(0.5, 0.5)
        this.time.advancedTiming = true
        this.load.setPreloadSprite(this.phaserImage)
        this.state.start('MainMenu')
    }
}