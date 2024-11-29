import speech_recognition as sr

try:
    while True :
        r = sr.Recognizer()
       
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.listen(source)
       
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            print("음성변환: " + stt)
            if "빨간색" in stt and "켜" in stt:
                print("빨간색 LED ON")
            elif "녹색" in stt and "켜" in stt:
                print("녹색 LED ON")
            elif "파란색" in stt and "켜" in stt:
                print("파란색 LED ON")
            elif "불" in stt and "꺼" in stt:
                print("모든 LED OFF")
               
            elif "끝" in stt or "종료" in stt:
                break
           
        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass
