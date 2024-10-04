import logo from './logo.svg';
import './App.css';

import { useState, useEffect} from 'react'

function App() {
  const [posts, setPosts] = useState([])

  useEffect(() => fetchPosts, [])

 function fetchPosts(){
  fetch(
    "http://127.0.0.1:5500/posts"
  )
  .then(res => res.json()
)
.then(postData => setPosts(postData))
}
console.log(posts)
  return (
    <div className="App">
      {posts.map(post => <h1>{post.content} </h1>)}
      </div>
  );
}

export default App;
