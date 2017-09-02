class Field {
    constructor(name, properties, plants) {
        if (typeof name != "string") {
            throw "Name of field has to be string";
        }
        else if (typeof properties != "object") {
            throw "Properties of field must be inside an object";
        }
        else if (typeof plants != "object") {
            throw "Plants of field must be an array of plants"
        }
        this.name = name
        this.properties = properties
        this.plants = plants
        this.grid = new Grid(10, [this.plants[0].texturePath, this.plants[1].texturePath])
        this.grid.setProps(0, 0, {"plant": 1})
    }

    checkEvent(event) {
        let prop, cond
        let apply = true
        for (prop in this.properties) {
            for (cond of event.conditions) {
                // for each prop we check if there is a condition with the same name
                if (prop == cond.name) {
                    // the condition has got name and func(prop)
                    // 
                    if (!(cond.func(this.properties[prop]))) {
                        apply = false
                        print("event cannot apply")
                    }
                }
            }
        }
        return apply
    }
    applyEvent(event) {
        let prop, mod, plant
        let apply = this.checkEvent(event)
        if (apply) {
            for (prop in this.properties) {
                for (mod in event.mods) {
                    if (prop == mod) { // For each prop we check if there is a mod with the same name
                        this.properties[prop] += event.mods[mod] // and we apply it

                    }
                }
            }
            for (plant of this.plants) {
                plant.applyEvent(event)
            }
        }
    }
}
