export default {
    MainDs: {
        labels :  ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"],
        values : Array.from({length: 20}, () => Math.floor(Math.random() * 80))
    },
}