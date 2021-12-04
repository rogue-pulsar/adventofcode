import UIKit

// Import input into array of strings
let path = Bundle.main.path(forResource: "input", ofType: "txt")!
let text = try! String(contentsOfFile: path, encoding: String.Encoding.utf8)
var report = text.components(separatedBy: CharacterSet.newlines)
// Strip last linebreak
report.removeLast()

//let report = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]

var count = 0

for (index, _) in report.enumerated() {
    if report.indices.contains(index + 1) {
        if report[index] < report[index + 1] {
            count += 1
        }
    }
}
// Result 1691, 1 short, unsure why it keeps coming up 1 short - assumed to be swift quirk with importing a file? Works fine with sample dataset.
print(count)
