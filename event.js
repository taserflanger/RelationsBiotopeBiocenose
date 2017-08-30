class Event {
    constructor(name, mods, conditions) {
        if (typeof mods != "object") {
            throw "mods of an event have to live in an object"
        } else if (typeof name != "string") {
            throw "name of event has to be a string"
        } else if (typeof conditions != "object") {
            throw "conditions of event have to live in an object"
        }
        this.name = name
        this.mods = mods
        this.conditions = conditions
    }
}