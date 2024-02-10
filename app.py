from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


def read_file_content(filename):
    with open(filename, 'r',encoding='utf-16') as file:
        return file.read()

def read_file_to_dict(filename):
    data_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                try:
                    key = int(parts[0].strip())
                    value = parts[1].strip()
                    data_dict[key] = value
                except ValueError:
                    print(f"Error: Invalid format in line '{line.strip()}'")
    return data_dict

@app.route('/api', methods=['GET'])
def api():
    # Get query parameters
    target = request.args.get('target')
    start = request.args.get('start')
    end = request.args.get('end')



    # if(start is not None and start <= 0):
    

    if target == 'file4':
        file_content = read_file_content('file4.txt')
        return render_template('index.html', file_content=file_content)


    if target is None or target == 'file1':
        filename = "file1.txt"
        data_dict = read_file_to_dict(filename)
        


        if(start is not None and end is not None):
            start = int(start)
            end = int(end)
        
            string = ""
            for key, value in data_dict.items():
                if(key>= start and key<=end):
                    string = string+' ' + value

        else:
            string = ""
            for key, value in data_dict.items():
                string = string+' ' + value    



        print(data_dict)
        return jsonify(string), 400
    
    if target == "file2":
        filename = "file2.txt"
        data_dict = read_file_to_dict(filename)
        
        string = ""

        for key, value in data_dict.items():
            string = string+' ' + value

        print(data_dict)
        return jsonify(string), 400   
    
    if target == "file3":
        filename = "file3.txt"
        data_dict = read_file_to_dict(filename)
        
        string = ""

        for key, value in data_dict.items():
            string = string+' ' + value

        print(data_dict)
        return jsonify(string), 400       
    
    



   

if __name__ == '__main__':
    app.run(debug=True)