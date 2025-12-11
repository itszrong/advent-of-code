use std::fs;

fn get_n (line: &str) -> usize {

    let elements = line.split_whitespace().collect::<Vec<_>>();
    
    let mut n = 0usize;
    let all_ops: Vec<&str> = elements[1..elements.len()-1].to_vec();
    let mut ops_vec: Vec<Vec<usize>> = vec![Vec::new(); all_ops.len()];
    for (i, op) in all_ops.into_iter().enumerate() {
        let op_vec: Vec<usize> = op[1..op.len()-1]
            .split(',')
            .map(|x| x.parse::<usize>().unwrap())
            .collect();
        ops_vec[i] = op_vec;
    }

    let joltage_str: &str = elements[elements.len()-1];
    let joltage_str_vec: Vec<&str> = joltage_str[1..joltage_str.len()-1].split(',').collect::<Vec<&str>>();
    let mut joltage_vec: Vec<usize> = joltage_str_vec.iter().map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();

    // println!("{:?}", joltage_vec);
    // println!("{:?}", ops_vec);

    while joltage_vec.iter().sum::<usize>() > 0 {
        let mut min_joltage: usize = *joltage_vec.iter().max().unwrap();
        let mut min_index: usize = 0;
        for (i, joltage) in joltage_vec.iter().enumerate() {
            if *joltage > 0 {
                if *joltage <= min_joltage {
                    min_index = i;
                    min_joltage = *joltage;
                }
            }
        }
        let mut index_longest_op: usize = 0;
        let mut longest_op: usize = 0;
        for (i, op) in ops_vec.iter().enumerate() {
            if op.contains(&min_index) {
                let mut check_each = 0;
                for &op_j in op.iter() {
                    if joltage_vec[op_j] > 0{
                        check_each += 1;
                    }
                }
                if check_each == op.len() && op.len() > longest_op {
                    longest_op = op.len();
                    index_longest_op = i;
                }
            }
        }
        for i in 0..joltage_vec.len() {
            if ops_vec[index_longest_op].contains(&i) {
                joltage_vec[i] -= min_joltage;
            }
        }
        if min_joltage > 100000 {
            return 0;
        }
        n += min_joltage;
    }
    n
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
