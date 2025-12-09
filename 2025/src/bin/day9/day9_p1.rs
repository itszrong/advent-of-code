use std::fs;
use std::cmp::max;

fn main() {
    let contents = fs::read_to_string("src/bin/day9/data.txt")
        .expect("Should have been able to read the file");

    let mut largest_area: i64 = 0;
    let mut points: Vec<Vec<i64>> = Vec::new();
    for line in contents.lines() {
        let point = line.split(',').map(str::trim).map(str::parse::<i64>).collect::<Result<Vec<i64>,_>>().unwrap();
        points.push(vec![point[0], point[1]]);
    }
    for (i, point1) in points.iter().enumerate() {
        for (j, point2) in points.iter().enumerate() {
            if i <= j {
                continue
            }
            let area = ((point1[0]-point2[0]).abs()+1)*((point1[1]-point2[1]).abs()+1);
            largest_area = max(largest_area, area);
        }
    }
    
    println!("{}", largest_area);
}
