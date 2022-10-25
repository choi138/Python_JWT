import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './Home'
import Login from './Login'
import Register from './Register'
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  )
}

export default App