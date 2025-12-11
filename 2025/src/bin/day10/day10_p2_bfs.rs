use std::fs;
use std::collections::VecDeque;
use std::collections::HashSet;

fn get_n (line: &str) -> usize {

    let elements = line.split_whitespace().collect::<Vec<_>>();
    
    let joltage_str: &str = elements[elements.len()-1];
    let joltage_str_vec: Vec<&str> = joltage_str[1..joltage_str.len()-1].split(',').collect::<Vec<&str>>();
    let joltage_vec: Vec<usize> = joltage_str_vec.iter().map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();

    let all_ops: Vec<&str> = elements[1..elements.len()-1].to_vec();
    let mut ops_vec: Vec<Vec<usize>> = vec![vec![0; joltage_vec.len()]; all_ops.len()];
    for (i, op) in all_ops.into_iter().enumerate() {
        let op_vec: Vec<usize> = op[1..op.len()-1]
            .split(',')
            .map(|x| x.parse::<usize>().unwrap())
            .collect::<Vec<usize>>();
        for op_j in op_vec {
            ops_vec[i][op_j] += 1;
        }
    }


    let start = vec![0; joltage_vec.len()];
    let mut queue = VecDeque::new();
    let mut seen = HashSet::new();

    queue.push_back((start.clone(), 0usize));
    seen.insert(start.clone());

    while let Some((state, n)) = queue.pop_front() {
        if state == joltage_vec {
            return n;
        }
        for op in ops_vec.iter() {
            let mut new_state = state.clone();
            for i in 0..joltage_vec.len() {
                if op[i] > 0 {
                    new_state[i] += 1;
                }
            }
            if !seen.contains(&new_state) {
                queue.push_back((new_state.clone(), n + 1));
                seen.insert(new_state.clone());
            }   
        }
    }
    0
}

fn main() {

    let contents = fs::read_to_string("src/bin/day10/data.txt")
        .expect("Should have been able to read the file");

    let mut res: usize = 0;
    for line in contents.lines() {
        let n = get_n(line);
        if n != 0 {
            println!("{}", n);
        }
        res += n;
    }
    println!("{}", res);
}
