let read_file filename =
  let ic = open_in filename in
  let rec read_lines acc =
    try
      let line = input_line ic in
      read_lines (line :: acc)
    with End_of_file ->
      close_in ic;
      List.rev acc
  in
  read_lines []

let () =
  let lines = read_file "day1/data_ex.txt" in
  List.iter (fun line -> Printf.printf "%s
" line) lines
