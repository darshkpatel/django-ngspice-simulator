// import 'react-dropzone-uploader/dist/styles.css'
import './css/uploadBox.css';
import Dropzone from 'react-dropzone-uploader'
import React, { Component } from 'react';

class UploadBox extends Component {
  constructor(props) {
    super(props);
    this.state = { 'files': [] }
    // specify upload params and url for your files
    this.getUploadParams = ({ meta }) => { return { url: 'http://localhost:8000/api/uploads/' } }

    // called every time a file's `status` changes
    this.handleChangeStatus = ({ meta, file }, status) => { console.log(status, meta, file) }

    // receives array of files that are done uploading when submit button is clicked
    this.handleSubmit = (files, allFiles) => {
      // console.log(files.map(f => f.xhr))

      files.forEach(file => {
        console.log(file.xhr)
        var task_id = JSON.parse(file.xhr['responseText'])['task_id'];
        console.log('Sending Start Request: ', task_id)
        this.StartTask(task_id);
      })
      files.forEach(file => { console.log(file) })
      this.props.updateMainState({
        'showResultCard': true, 'files': files.map(file => {
          return {
            'fileName': file.meta.name,
            'fileID': JSON.parse(file.xhr.responseText).files_set[0].file_id,
            'response': JSON.parse(file.xhr.responseText)
          }
        })
      })
      // allFiles.forEach(f => f.remove())
    }
    console.log(props)

    this.StartTask = (TaskID) => {
      var xhr = new XMLHttpRequest()
      xhr.responseType = 'json';
      xhr.open('GET', 'http://localhost:8000/api/task/' + TaskID + '/start', true);

      // const self = this;
      // xhr.onload = function () {
      //   var jsonResponse = xhr.response;
      //   //  self.setState({'files':newFiles})
      //   //  self.props.updateMainState({'showResultCard': true, 'files':self.state.files})


      // };
      xhr.send()
      console.log('Sent Request for ', TaskID)
    }
  }




  render() {
    return (

      <div className="">
        <Dropzone
          getUploadParams={this.getUploadParams}
          onChangeStatus={this.handleChangeStatus}
          onSubmit={this.handleSubmit}
          className="dropzone"
        />
      </div>
    )
  }
}
export default UploadBox;