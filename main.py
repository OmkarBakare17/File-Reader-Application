from flask import Flask, request, render_template
import chardet

app = Flask(__name__)

@app.route('/<filename>', methods=['GET'])
def read_files(filename):
    try:
        path = f'test_files/{filename}'
        try:
            with open(path, 'rb') as f:
                encoding = chardet.detect(f.read())['encoding']
            
            with open(path, 'r', encoding=encoding) as file:
                content_data = file.readlines()
        except FileNotFoundError as e:
            print(f"Error reading file: {e}")
            return render_template("error.html", error_message = f"No such file or directory: '{filename}'")

        start_line = request.args.get('start_line', type=int)
        end_line = request.args.get('end_line', type=int)

        if start_line is not None and end_line is not None:
            content_data = content_data[start_line - 1 : end_line]

        data = ''.join(content_data)
        
        return render_template("file.html", content=data)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return render_template("error.html", error_message="Unexpected error")

if __name__ == '__main__':
    app.run(debug=True)
