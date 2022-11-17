import React, { useState } from 'react'
import "../styles/app.css";


const App = () => {
  const [data, setData] = useState([])

  const getData = async () => {
    await fetch("/chooser").then(
      res => res.json()
    ).then(data => {
      setData(data)
    })
  }

  return (
    <div className="App">
      <button type='submit' onClick={getData}>Pick!</button>
      <div>
      {data.map((data) => {
        return (
          <div>
            <h1>{data}</h1>
          </div>
        )
      })}
      </div>
    </div>
    );
}

export default App;
