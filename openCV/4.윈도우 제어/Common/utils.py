def print_matInfo(name, image):
    if image.dtype == 'uint8':  # 데이터타입 확인
        mat_type = "CV_8U"
    elif image.dtype == 'int8':
        mat_type = "CV_8S"
    elif image.dtype == 'uint16':
        mat_type = "CV_16U"
    elif image.dtype == 'int16':
        mat_type = "CV_16S"
    elif image.dtype == 'float32':
        mat_type = "CV_32F"
    elif image.dtype == 'float64':
        mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1  # 이미지 체널 확인(RGB(3ch)인지 흑백(1ch)인지)

    # depth, channel 출력
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type, nchannel))