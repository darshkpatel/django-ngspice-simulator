import React from 'react';
import {useDropzone} from 'react-dropzone';

function UploadBox(props) {
  const {acceptedFiles, getRootProps, getInputProps} = useDropzone({
    disabled: true
  });

  const files = acceptedFiles.map(file => (
    <li key={file.name}>
      {file.name} - {file.size} bytes
    </li>
  ));

  return (
    <section className="container">
      <div {...getRootProps({className: 'dropzone disabled'})}>
        <input {...getInputProps()} />
        <p>Drag 'n' drop some files here, or click to select files</p>
      </div>
      <aside>
        <h4>Files</h4>
        <ul>{files}</ul>
      </aside>
    </section>
  );
}

{/* <UploadBox /> */}

export default UploadBox;