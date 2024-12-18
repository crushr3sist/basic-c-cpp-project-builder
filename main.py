import os
import pathlib
import shutil
import subprocess


def build_project():
    # Determine paths
    script_dir = pathlib.Path(__file__).parent.resolve()
    src_dir = script_dir / "src"
    build_dir = script_dir / "build"

    # Cleanup build directory
    if build_dir.exists():
        shutil.rmtree(build_dir)

    # Create build directory
    build_dir.mkdir(exist_ok=True)
    os.chdir(build_dir)

    # Find source files
    src_files = [str(file) for file in src_dir.rglob("*.cpp")]
    c_files = [str(file) for file in src_dir.rglob("*.c")]
    print(c_files)

    if not src_files and not c_files:
        print("No source files found.")
        return False

    # Compile source files
    for file in src_files:
        obj_file = pathlib.Path(file).name.replace(".cpp", ".o")
        compile_cmd = f"g++ -c {file} -o {obj_file} -I{src_dir}"
        print(f"compiling: {file}")
        if subprocess.run(compile_cmd, shell=True).returncode != 0:
            print(f"Compilation failed for {file}")
            return False

    for file in c_files:
        obj_file = pathlib.Path(file).name.replace(".c", ".o")
        compile_cmd = f"gcc -c {file} -o {obj_file} -I{src_dir}"
        print(f"compiling: {file}")
        if subprocess.run(compile_cmd, shell=True).returncode != 0:
            print(f"Compilation failed for {file}")
            return False

    # Link object files
    obj_files = [pathlib.Path(file).name.replace(".cpp", ".o") for file in src_files]
    obj_files += [pathlib.Path(file).name.replace(".c", ".o") for file in c_files]
    link_cmd = f"g++ -o proj.exe {' '.join(obj_files)}"

    if subprocess.run(link_cmd, shell=True).returncode != 0:
        print("Linking failed")
        return False

    # Cleanup object files
    for obj_file in obj_files:
        os.remove(obj_file)

    print("Build successful!")
    return True


if __name__ == "__main__":
    build_project()
