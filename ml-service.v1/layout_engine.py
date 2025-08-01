def detect_layout(image, method="none"):
    if method == "layoutparser":
        import layoutparser as lp
        model = lp.Detectron2LayoutModel("lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config")
        return model.detect(image)
    return None
