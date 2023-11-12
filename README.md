# The Omniscient One

**Description:**
The Omniscient One, or 2 for short, is a Language Model (LLM) based on OpenAI's GPT3.5 Turbo model. It utilizes the Llama Index package to vectorize textual data from various file formats such as `.html`, `.txt`, `.pdf`, `.docx`, and even `.png/.jpg` through OCR (Optical Character Recognition). Additionally, it supports YouTube links for transcript extraction.

## Functionality

### How It Works:
The Llama Index is employed to vectorize textual data, allowing the GPT 3.5 Turbo model to comprehend it effectively. This process is akin to training the model on custom data.

### Supported Formats:
1. **PDF:** ![PDF Example](https://media.discordapp.net/attachments/1172568946013110346/1173193687518421092/image.png?ex=656310c3&is=65509bc3&hm=766e378bdec5fced8da35b75cf1f5e1fd789008e70dfd0eb34e8094e001412e6&=&width=997&height=942)

2. **Text:** ![Text Example](https://media.discordapp.net/attachments/1172568946013110346/1172970724009455707/image.png?ex=6562411d&is=654fcc1d&hm=74833934acbe0153e115c6a9b73d2b9b7624055255416322c8c66d4e29528d7d&=&width=921&height=942)

3. **Microsoft Word Document:** ![Word Example](https://media.discordapp.net/attachments/1172568946013110346/1172972894716960768/image.png?ex=65624322&is=654fce22&hm=d266fe2b986200dfb42260881a7fdb97813f003cf5208c6884926e78f381fb25&=&width=1033&height=940)

4. **Images (OCR):** ![OCR Example](https://media.discordapp.net/attachments/1172568946013110346/1173282532368863282/image.png?ex=65636382&is=6550ee82&hm=358a42bac9310cadb20234b178d091d7762698a7c759b26f49065aaee0bb90ce&=&width=1041&height=942)

5. **YouTube Links (Transcript):** ![Transcript Example](https://media.discordapp.net/attachments/1172568946013110346/1172983524073160806/image.png?ex=65624d09&is=654fd809&hm=d821e538d7ca6c05e9c6a1947d08793990bcdf80ff3cdc55c7eec0bc6f9aaa4b&=&width=886&height=942)

## Requirements
1. `python3.8` or above
2. [Streamlit](https://streamlit.io/)
3. [Llama Index](https://www.llamaindex.ai/)
4. [OpenAI Python Wrapper](https://pypi.org/project/openai/)
5. [EasyOCR](https://github.com/JaidedAI/EasyOCR)
6. [PyPDF2](https://pypi.org/project/PyPDF2/)
7. [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)

**Developers:** 
- [me](https://divine-architect.xyz)
- Yash Sharma [RVCE]
