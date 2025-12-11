use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("src/bin/day11/data.txt")
        .expect("Should have been able to read the file");

    let mut graph: HashMap<&str, Vec<&str>> = HashMap::new();
    for line in contents.lines() {
        let parts = line.split(":").collect::<Vec<&str>>();
        let key = parts[0];
        let values = parts[1].split_whitespace().collect::<Vec<&str>>();
        graph.insert(key, values);
    }
 
    fn path_find(graph: &HashMap<&str, Vec<&str>>, beginning: &str, end: &str, avoid: &[&str]) -> usize {

        let mut current_store: HashMap<&str, usize> = HashMap::new();
        current_store.insert(beginning, 1);
        let empty_store: HashMap<&str, usize> = HashMap::new();
        let mut no_end = 0usize;
        while current_store.len() > 0 {
            let mut new_store = empty_store.clone();
            for (&key, &value) in current_store.iter() {
                let next_nodes = graph.get(&key).unwrap();
                for next_node in next_nodes {
                    if avoid.contains(next_node) {
                        continue
                    }
                    if next_node == &end {
                        no_end += value;
                        continue
                    }
                    *new_store.entry(*next_node).or_insert(0) += value;
                }
            }
            current_store = new_store;
        }

        return no_end;
    }

    let paths_svr_dac = path_find(&graph, "svr", "dac", &["fft", "out"]);
    let paths_dac_fft = path_find(&graph, "dac", "fft", &["out", "svr"]);
    let paths_fft_out = path_find(&graph, "fft", "out", &["dac", "svr"]);
    let paths_svr_fft = path_find(&graph, "svr", "fft", &["dac", "out"]);
    let paths_fft_dac = path_find(&graph, "fft", "dac", &["out", "svr"]);
    let paths_dac_out = path_find(&graph, "dac", "out", &["fft", "svr"]);
    
    println!("{:?}", paths_svr_dac * paths_dac_fft * paths_fft_out + paths_svr_fft * paths_fft_dac * paths_dac_out);
}
