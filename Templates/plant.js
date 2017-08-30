class Plant {
    constructor(name, properties) {
        if (typeof name != "string") {
            throw "Name of plant has to be string";
        }
        else if (typeof properties != "object") {
            throw "Properties of plant must be inside an object";
        }
        this.name = name;
        this.properties = properties;
    }
}