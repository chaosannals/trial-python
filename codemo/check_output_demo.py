
from subprocess import check_output, CalledProcessError
from chardet import detect

def main():
    '''
    
    '''


    try:
        out_bytes = check_output(
            ['ping', '114.114.114.114'],
        )
        code = 0
    except CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode

    cd = detect(out_bytes)
    print(cd)
    out_text = out_bytes.decode(
        cd['encoding']
    )
    print(out_text)


if '__main__' == __name__:
    main()