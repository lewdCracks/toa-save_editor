use serde_json::{self, json};
use std::fs;
use std::io::{self, prelude::*, BufReader};
use std::path::Path;
use zip::ZipArchive;

fn main() -> io::Result<()> {
    let enc_file = return_file("script/encounters.json");
    let reader = BufReader::new(enc_file);

    let prof_file = match fs::File::open(".toa-data/profile.json") {
        Ok(n) => n,
        Err(error) => {
            println!("Problem opening file : {}", error);
            std::process::exit(0)
        }
    };

    let mut prof_j: serde_json::Value = match serde_json::from_reader(prof_file) {
        Ok(n) => n,
        Err(error) => {
            println!("JSON file is not properly formatted!\nEr : {}", error);
            pause();
            std::process::exit(0)
        }
    };

    prof_j["animatedCgSeen"]["HARPY_ELITE_ANAL"] = json!(1);

    let mut count = 0;
    for line in reader.lines() {
        match line {
            Ok(n) => {
                if n.contains("foreground") { // Still need to add a way to get enemy knowledge through scripting
                    let inter = get_val(n);

                    if prof_j["cgSeen"][inter.clone()].to_string().contains("null") { // Could probably reduce use of .clone
                        prof_j["cgSeen"][inter.clone()] = json!(1);
                        println!("ADDED {}", inter);
                        count += 1;
                    }
                } else if n.contains("animatedForeground") {
                    let inter = get_val(n);
                    if prof_j["animatedCgSeen"][inter.clone()]
                        .to_string()
                        .contains("null")
                    {
                        prof_j["animatedCgSeen"][inter.clone()] = json!(1); // See if json! marco is best way to convert
                        println!("ADDED {}", inter);
                        count += 1;
                    }
                } else {
                    // Could add unchanged variable to return 
                }
            }
            Err(error) => {
                println!("Error {}", error);
                pause();
            }
        };
    }
    println!("Added a total of {} new pieces of content!", count); // + {x} amount unchanged

    let prof_file = fs::File::create(".toa-data/profile.json");

    serde_json::to_writer(prof_file?, &prof_j).expect("Failed to write!"); // Could probably have a match case here instead of just panicking 

    pause();

    Ok(())
}

fn get_val(val: String) -> String {
    let vec: Vec<&str> = val.split(":").collect();
    vec[1].trim().replace("\"", "").replace(",", "").to_string()
}

fn return_file(path: &str) -> fs::File {
    if Path::new(path).exists() {
        match fs::File::open(path) {
            Ok(n) => return n,
            Err(error) => {
                println!("Ran into an error : {}", error);
                pause();
                std::process::exit(0)
            }
        };
    } else {
        extract_enc();
        match fs::File::open("script/encounters.json") { // I also don't know if it's standard fare to use match statements everywhere that a Result is returned - like wtf????
            Ok(n) => return n,                           // --  So past me is dumb and people use unwrap if they really think that no error will be thrown-
            Err(error) => {                              // --- match still seems like such a nice error handling tho~
                println!("Ran into an error : {}", error);
                pause();
                std::process::exit(0)
            }
        }
    }
}

fn extract_enc() {
    let zipfile = std::fs::File::open("TalesOfAndrogyny.jar").unwrap(); // I'm fucking dumb - .unwrap is literally the opposite of .expect
    let mut archive = ZipArchive::new(zipfile).unwrap();

    // Basically just a gutted version of "https://github.com/zip-rs/zip/blob/master/examples/extract.rs", still trying to understand everything 
    // because I literally have no idea how rust works lmao (fucking python pleb)...
    let mut file = archive.by_name("script/encounters.json").unwrap();
    #[allow(deprecated)]
    let outpath = file.sanitized_name();

    if (&*file.name()).ends_with('/') {
        fs::create_dir_all(&outpath).unwrap(); // I also don't know how to properly use fs::create_dir_all in conjunction with a ZipFile all I was able to do was make folders -__-
    } else {
        if let Some(p) = outpath.parent() { // No fucking clue what the .parent operator does
            if !p.exists() {
                fs::create_dir_all(&p).unwrap();
            }
        }
        let mut outfile = fs::File::create(&outpath).unwrap();
        io::copy(&mut file, &mut outfile).unwrap(); // This copies the file data into the output files.
    }
}

fn pause() {
    let mut stdin = io::stdin();
    let mut stdout = io::stdout();

    write!(stdout, "Press ENTER when done...").unwrap();
    stdout.flush().unwrap();

    let _ = stdin.read(&mut [0u8]).unwrap();
}
