use std::cmp::max;
use std::collections::HashSet;
use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day9/data.txt")
        .expect("Should have been able to read the file");

    let mut rows: usize = 0;
    let mut cols: usize = 0;
    let mut points: Vec<Vec<usize>> = Vec::new();

    for line in contents.lines() {
        let point = line
            .split(',')
            .map(str::trim)
            .map(str::parse::<usize>)
            .collect::<Result<Vec<usize>, _>>()
            .unwrap();
        points.push(vec![point[0], point[1]]);
    }

    for p in points.iter() {
        rows = max(rows, p[0] + 2);
        cols = max(cols, p[1] + 2);
    }

    fn point_on_segment(px: f64, py: f64, x1: f64, y1: f64, x2: f64, y2: f64) -> bool {
        let cross = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1);
        if cross.abs() > 1e-9 {
            return false;
        }

        let min_x = x1.min(x2);
        let max_x = x1.max(x2);
        let min_y = y1.min(y2);
        let max_y = y1.max(y2);

        px >= min_x - 1e-9
            && px <= max_x + 1e-9
            && py >= min_y - 1e-9
            && py <= max_y + 1e-9
    }

    fn point_in_loop(px: f64, py: f64, points: &[Vec<usize>]) -> bool {
        let n = points.len();
        let mut inside = false;

        for i in 0..n {
            let p1 = &points[i];
            let p2 = &points[(i + 1) % n];
            let x1 = p1[0] as f64;
            let y1 = p1[1] as f64;
            let x2 = p2[0] as f64;
            let y2 = p2[1] as f64;

            if point_on_segment(px, py, x1, y1, x2, y2) {
                return true;
            }

            let intersects = (y1 > py) != (y2 > py);
            if intersects {
                let x_intersect = x1 + (py - y1) * (x2 - x1) / (y2 - y1);
                if x_intersect > px {
                    inside = !inside;
                }
            }
        }

        inside
    }

    fn compress_coords(points: &[Vec<usize>]) -> (Vec<i64>, Vec<i64>, Vec<Vec<bool>>) {
        let mut xs: Vec<i64> = points.iter().map(|p| p[0] as i64).collect();
        let mut ys: Vec<i64> = points.iter().map(|p| p[1] as i64).collect();
        xs.sort();
        xs.dedup();
        ys.sort();
        ys.dedup();

        let w = xs.len() - 1;
        let h = ys.len() - 1;

        let mut inside = vec![vec![false; w]; h];

        for j in 0..h {
            for i in 0..w {
                let cx = (xs[i] + xs[i + 1]) as f64 * 0.5;
                let cy = (ys[j] + ys[j + 1]) as f64 * 0.5;
                inside[j][i] = point_in_loop(cx, cy, points);
            }
        }

        (xs, ys, inside)
    }

    fn max_rectangle_with_points(
        xs: &[i64],
        ys: &[i64],
        inside: &[Vec<bool>],
        points_set: &HashSet<(i64, i64)>,
    ) -> i64 {
        let h = ys.len() - 1;
        let w = xs.len() - 1;

        let mut prefix = vec![vec![0i64; w + 1]; h + 1];
        for j in 0..h {
            for i in 0..w {
                prefix[j + 1][i + 1] = prefix[j + 1][i] + prefix[j][i + 1] - prefix[j][i]
                    + if inside[j][i] { 1 } else { 0 };
            }
        }

        let all_inside = |j1: usize, j2: usize, i1: usize, i2: usize| -> bool {
            let total = prefix[j2][i2] - prefix[j2][i1] - prefix[j1][i2] + prefix[j1][i1];
            let expected = ((j2 - j1) * (i2 - i1)) as i64;
            total == expected
        };

        let x_to_idx: std::collections::HashMap<i64, usize> =
            xs.iter().enumerate().map(|(i, &x)| (x, i)).collect();
        let y_to_idx: std::collections::HashMap<i64, usize> =
            ys.iter().enumerate().map(|(j, &y)| (y, j)).collect();

        let mut best_area = 0i64;

        let points_vec: Vec<(i64, i64)> = points_set.iter().cloned().collect();
        for i in 0..points_vec.len() {
            for j in (i + 1)..points_vec.len() {
                let (x1, y1) = points_vec[i];
                let (x2, y2) = points_vec[j];

                if x1 == x2 || y1 == y2 {
                    continue;
                }

                let x_l = x1.min(x2);
                let x_r = x1.max(x2);
                let y_b = y1.min(y2);
                let y_t = y1.max(y2);

                let Some(&i_l) = x_to_idx.get(&x_l) else { continue };
                let Some(&i_r) = x_to_idx.get(&x_r) else { continue };
                let Some(&j_b) = y_to_idx.get(&y_b) else { continue };
                let Some(&j_t) = y_to_idx.get(&y_t) else { continue };

                if all_inside(j_b, j_t, i_l, i_r) {
                    let area = (x_r - x_l + 1) * (y_t - y_b + 1);
                    if area > best_area {
                        best_area = area;
                    }
                }
            }
        }

        best_area
    }

    let (xs, ys, inside) = compress_coords(&points);

    let points_set: HashSet<(i64, i64)> = points
        .iter()
        .map(|p| (p[0] as i64, p[1] as i64))
        .collect();

    let largest_area = max_rectangle_with_points(&xs, &ys, &inside, &points_set);

    println!("{}", largest_area);
}
