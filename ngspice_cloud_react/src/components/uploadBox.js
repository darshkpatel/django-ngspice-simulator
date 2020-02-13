// import 'react-dropzone-uploader/dist/styles.css'
import './css/uploadBox.css';
import Dropzone from 'react-dropzone-uploader'
import React ,{Component} from 'react';

class UploadBox extends Component {
  constructor(){
    super();
  // specify upload params and url for your files
  this.getUploadParams = ({ meta }) => { return { url: 'https://httpbin.org/post' } }
  
  // called every time a file's `status` changes
  this.handleChangeStatus = ({ meta, file }, status) => { console.log(status, meta, file) }
  
  // receives array of files that are done uploading when submit button is clicked
  this.handleSubmit = (files, allFiles) => {
    console.log(files.map(f => f.meta))
    allFiles.forEach(f => f.remove())
  }
}

  render(){
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