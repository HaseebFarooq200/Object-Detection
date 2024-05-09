import './App.css';
import "primereact/resources/themes/lara-light-indigo/theme.css";
import "primereact/resources/primereact.min.css";
import React from 'react';
import { FileUpload } from 'primereact/fileupload';
        
function App() {
  // const [downloadUrl, setDownloadUrl] = useState(null);

  // // Function to trigger file download
  // const downloadFile = () => {
  //   if (downloadUrl) { 
  //     window.open(downloadUrl); // Open the download URL in a new tab/window
  //   }
  // };
  return (
    <div className="App">
     <h2>HELLO</h2>
     <FileUpload 
     name="test_file" 
     url={'/api/detect'} 
     multiple 
     accept="image/*" 
     maxFileSize={1000000} 
     emptyTemplate={<p className="m-0">Drag and drop files to here to upload.</p>} />
     
     {/* <button onClick={downloadFile}>Download Processed File</button> */}

    </div>
  );
}

export default App;


// import './App.css';
// import "primereact/resources/themes/lara-light-indigo/theme.css";
// import "primereact/resources/primereact.min.css";
// import React, { useState } from 'react';
// import { FileUpload } from 'primereact/fileupload';

// function App() {
//   const [downloadUrl, setDownloadUrl] = useState(null);

//   // Function to handle file upload
//   const onFileUpload = (event) => {
//     const formData = new FormData();
//     formData.append('test_file', event.files[0]);

//     fetch('/api/detect', {
//       method: 'POST',
//       body: formData,
//     })
//       .then(response => {
//         if (!response.ok) {
//           throw new Error('Network response was not ok');
//         }
//         return response.json();
//       })
//       .then(data => {
//         // Assuming your Flask backend responds with the download URL
//         const { download_url } = data;
//         setDownloadUrl(download_url); // Save the download URL
//       })
//       .catch(error => {
//         console.error('Error uploading file:', error);
//       });
//   };

//   // Function to trigger file download
//   const downloadFile = () => {
//     if (downloadUrl) {
//       window.open(downloadUrl); // Open the download URL in a new tab/window
//     }
//   };

//   return (
//     <div className="App">
//       <h2>HELLO</h2>
//       <FileUpload 
//         name="test_file" 
//         url="/api/detect" 
//         multiple={false} 
//         accept="image/*" 
//         maxFileSize={1000000} 
//         emptyTemplate={<p className="m-0">Drag and drop files here to upload.</p>} 
//         onUpload={onFileUpload} />
//       <button onClick={downloadFile}>Download Processed File</button>
//     </div>
//   );
// }

// export default App;
