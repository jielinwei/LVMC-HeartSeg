import argparse, time

def run_inference(input_path, output_path):
    print(f"[LVMC-HeartSeg] Inference stub on: {input_path}")
    # TODO: load trained weights and perform segmentation
    time.sleep(0.5)
    print(f"[LVMC-HeartSeg] Saved segmentation mask to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    run_inference(args.input, args.output)
