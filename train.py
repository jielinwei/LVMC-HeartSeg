import argparse, yaml, time

def train(cfg):
    print("[LVMC-HeartSeg] Training started with hyperparameters:")
    print(yaml.dump(cfg, sort_keys=False))
    # TODO: implement dataset, model, loss, optimizer, trainer
    time.sleep(1)
    print("[LVMC-HeartSeg] Training finished (stub). Check ./results for outputs.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/training_hyperparameters.yaml")
    args = parser.parse_args()
    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)
    train(cfg)
