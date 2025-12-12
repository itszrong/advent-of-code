use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day12/data.txt")
        .expect("Should have been able to read the file");

    let parts: Vec<&str> = contents.split("\n\n").collect::<Vec<&str>>();
    let regions = parts[parts.len()-1];
    let mut res = 0usize;
    for region in regions.lines() {
        if let Some((dims, values)) = region.split_once(":") {
            let (width, height) = dims.split_once("x").unwrap();
            let width = width.parse::<usize>().unwrap();
            let height = height.parse::<usize>().unwrap();
            if width*height >= 9*values.split_whitespace().map(|x| x.parse::<usize>().unwrap()).sum::<usize>() {
                res += 1;
            }
        }
    }
    println!("{:?}", res);
}
