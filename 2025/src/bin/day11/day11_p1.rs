use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;

fn main() {
    let contents = fs::read_to_string("src/bin/day11/data.txt")
        .expect("Should have been able to read the file");

    let mut graph: HashMap<&str, Vec<&str>> = HashMap::new();
    let mut paths: HashSet<Vec<&str>> = HashSet::new();
    let mut queue: VecDeque<Vec<&str>> = VecDeque::new();
    for line in contents.lines() {
        let parts = line.split(":").collect::<Vec<&str>>();
        let key = parts[0];
        let values = parts[1].split_whitespace().collect::<Vec<&str>>();
        graph.insert(key, values);
    }
    queue.push_back(vec!["you"]);
    while let Some(path) = queue.pop_front() {
        if path.last().unwrap() == &"out" {
            paths.insert(path.clone());
            continue;
        }
        let next_nodes = graph.get(path.last().unwrap()).unwrap();
        for next_node in next_nodes {
            let mut new_path = path.clone();
            new_path.push(*next_node);
            queue.push_back(new_path);
        }
    }
    println!("{:?}", paths.len());
}
