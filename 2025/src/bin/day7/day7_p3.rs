use std::fs;

fn main() {

    let contents = fs::read_to_string("src/bin/day7/data.txt")
        .expect("Should have been able to read the file");

    let mut beam_vec: Vec<i64> = vec![0; contents.lines().next().unwrap().len()];
    for line in contents.lines() {
        for (i, coor) in line.chars().enumerate() {
            if coor == 'S' {
                beam_vec[i] = 1;
            }
            if coor == '^' && beam_vec[i] != 0 {
                beam_vec[i-1] += beam_vec[i];
                beam_vec[i+1] += beam_vec[i];
                beam_vec[i] = 0;
            }
        }
    }
    println!("{}", beam_vec.into_iter().sum::<i64>());
}
