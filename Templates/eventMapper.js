function eventMapper(toMap) {
    let events = []
    for (map of toMap) {
        events.push(new Event(map[0], map[1], map[2]))
    }
    return events
}