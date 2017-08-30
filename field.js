class Field {
    constructor(name, properties) {
        if (typeof name != "string") {
            throw "Name of field has to be string";
        }
        else if (typeof properties != "object") {
            throw "Properties of field must be inside an object";
        }
        this.name = name;
        this.properties = properties;
    }

    checkEvent(event) {
        let prop, cond
        let apply = true
        for (prop in this.properties) {
            for (cond of event.conditions) {
                if (prop == cond.name) {
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
        let prop, mod
        let apply = this.checkEvent(event)
        if (apply) {
            for (prop in this.properties) {
                for (mod in event.mods) {
                    if (prop == mod) { // For each prop we check if there is a mod with the same name
                        this.properties[prop] += event.mods[mod] // and we apply it

                    }
                }
            }
        }
    }
}
