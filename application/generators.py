import qrcode

def create_qr_code(data, size=10, border=0):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image()


def create_link(request, application_id):
    link = f"{request.scheme}://{request.META['HTTP_HOST']}/application/access-with-qrcode/{application_id}"
    return link