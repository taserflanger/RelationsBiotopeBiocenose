class Plant {
    constructor(name, properties, ideal_conditions) {
        if (typeof name != "string") {
            throw "Name of plant has to be string";
        }
        else if (typeof properties != "object") {
            throw "Properties of plant must be inside an object";
        }
        else if (typeof ideal_conditions != "object") {
            throw "Ideal conditions of plant must be inside an object"
        }
        this.name = name
        this.properties = properties
        this.ideal_conditions = ideal_conditions
    }
    applyEvent(event) {
        let prop, mod
        for (prop in this.ideal_conditions) {
            for (mod in event.mods) {
                if (prop == mod) { // For each prop we check if there is a mod with the same name
                    this.ideal_conditions[prop] += event.mods[mod] // and we apply it
                }
            }
        }
    }
}