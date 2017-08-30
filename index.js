let debug = true

window.onload = function () {

    //  Note that this html file is set to pull down Phaser 2.5.0 from the JS Delivr CDN.
    //  Although it will work fine with this tutorial, it's almost certainly not the most current version.
    //  Be sure to replace it with an updated version before you start experimenting with adding your own code.
    
    let game = new Phaser.Game(800, 600, Phaser.AUTO, 'container')
    game.state.add('Boot', Game.Boot)
    game.state.add('Preloader', Game.Preloader)
    game.state.add('MainMenu', Game.MainMenu)
    game.state.add('MapSansouire', Game.MapSansouire)

    game.state.start('Boot')
}