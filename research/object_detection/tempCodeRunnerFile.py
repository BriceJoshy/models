
    category_index = label_map_util.create_category_index_from_labelmap(args.labelmap, use_display_name=True)

    run_inference(detection_model, category_index, args.image_path)

# Command to start script
#  python .\detect_from_images.py -m ssd_mobilenet_v2_320x320_coco17_tpu-8\saved_model -l .\data\mscoco_label_map.pbtxt -i .\test_images