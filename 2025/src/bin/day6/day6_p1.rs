use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day6/data.txt")
        .expect("Should have been able to read the file");

    let mut nums: Vec<&str> = contents.lines().collect::<Vec<&str>>();
    let operators: Vec<&str> = nums.pop().unwrap().split_whitespace().collect::<Vec<&str>>();
    let mut total_sum = 0;
    for i in 0..operators.len() {
        let mut sum = 0;
        for line in nums.iter() {
            let num = line.split_whitespace().collect::<Vec<&str>>()[i];
            if operators[i] == "+" {
                if sum == 0 {
                    sum = num.parse::<i64>().unwrap();
                } else {
                    sum += num.parse::<i64>().unwrap();
                }   
            } else if operators[i] == "*" {
                if sum == 0 {
                    sum = num.parse::<i64>().unwrap();
                } else {
                    sum *= num.parse::<i64>().unwrap();
                }
            }
        }
        total_sum += sum;
    }
    println!("{:?}", total_sum);
}
