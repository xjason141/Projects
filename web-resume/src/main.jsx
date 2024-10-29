import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import MyApp from './components/Profile'
import 'bootstrap/dist/css/bootstrap.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <MyApp />
  </StrictMode>,
)
