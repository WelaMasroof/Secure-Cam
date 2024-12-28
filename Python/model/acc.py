from ultralytics import YOLO

# Load the trained model
model = YOLO("D:\SecuirtyCam\SecuirtyCam\Python\model\best.pt")

# Run validation
results = model.val(data="C:\Users\Faaez\Downloads\data.yaml")  # Use test or validation set
