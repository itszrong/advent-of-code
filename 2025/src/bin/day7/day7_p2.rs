use std::fs;
use std::collections::HashMap;

fn main() {

    let contents = fs::read_to_string("src/bin/day7/data.txt")
        .expect("Should have been able to read the file");

    let mut beam_map = HashMap::with_capacity(contents.lines().next().unwrap().len());
    for line in contents.lines() {
        for (i, coor) in line.chars().enumerate() {
            if beam_map.get(&i) == None {
                beam_map.insert(i, 0);
            }
            if coor == 'S' {
                beam_map.insert(i, 1);
            }
            let coor_val: i64 = *beam_map.get(&i).unwrap();
            if coor == '^' && coor_val != 0 {
                *beam_map.get_mut(&(i-1)).unwrap() += coor_val;
                *beam_map.get_mut(&(i+1)).unwrap() += coor_val;
                *beam_map.get_mut(&i).unwrap() = 0;
            }
        }
    }
    let total: i64 = beam_map.values().sum();
    println!("{}", total);
}
