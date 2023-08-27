import React from 'react';
import { AiOutlineInfoCircle, AiOutlineSearch, AiOutlineHome, AiFillCaretDown } from 'react-icons/ai'
import Link from "../components/Link";


function Navbar() {
  return (
    
    <nav className="bg-neutral-800 shadow-lg">
      <div className="container mx-auto flex justify-between items-center ">
        
        <div className="flex space-x-4 items-center h-full">
          
          <div className="relative">            
            <div className="relative z-20 bg-white px-9 p-1" style={{ 
              clipPath: 'polygon(0% 0%, 80% 0%, 100% 100%, 20% 100%)',
            }}>
              <a href="/" className="text-red-600 text-2xl font-bold font-sans md:font-serif hover:italic">The Verdict</a>
            </div>
          </div>
          
          
          <ul className="flex space-x-4 ml-4">
            <li><Link to="/movies" href="#" >Movies <AiFillCaretDown className="ml-2 mt-1"/></Link></li>
            <li><Link to="/shows" href="#" >Shows <AiFillCaretDown className="ml-2 mt-1"/></Link></li>
            <li><Link to="/games" href="#" >Games <AiFillCaretDown className="ml-2 mt-1"/></Link></li>
            <li><Link to="/hardware" href="#" >Hardware <AiFillCaretDown className="ml-2 mt-1"/></Link></li>
          </ul>
        </div>
  
        <div>
          <ul className="flex space-x-4">
            <li><a href="#" className="text-white hover:text-red-600"><AiOutlineHome className="text-xl" /></a></li>
            <li><a href="#" className="text-white hover:text-red-600"><AiOutlineInfoCircle className="text-xl" /></a></li>
            <li><a href="#" className="text-white hover:text-red-600"><AiOutlineSearch className="text-xl"/> </a></li>
          </ul>
        </div>

      </div>
    </nav>
  );
}

export default Navbar;


