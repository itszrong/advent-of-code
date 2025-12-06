use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day6/data.txt")
        .expect("Should have been able to read the file");

    let mut nums: Vec<&str> = contents.lines().collect::<Vec<&str>>();
    let operators: String = nums.pop().unwrap().to_string();
    let mut total_sum = 0;
    let mut curr_operator = ' ';
    let mut sum = 0;
    for (i, operator) in operators.chars().enumerate() {
        if operator != ' ' {
            total_sum += sum;
            curr_operator = operator;
            sum = 0;
        }
        let mut num = String::new();
        for line in nums.iter() {
            num.push(line.chars().nth(i).unwrap());
        }
        if !num.trim().is_empty() {
            let num_i = num.trim().parse::<i64>().unwrap();
            if sum == 0 {
                sum = num_i;
            } else {
                if curr_operator == '+' {
                        sum += num_i;
                } else if curr_operator == '*' {
                    sum *= num_i;
                }
            }
        }
    }
    total_sum += sum;
    println!("{:?}", total_sum);
}
