// LinksCard.jsx

function LinksCard({ spotLight, title }) {
  return (
      <div 
          className="card bg-white p-4 rounded-md shadow-md my-4 cursor-pointer"
      >
        <h3>{spotLight}</h3>
        <hr className="my-4 border-t border-gray-300" />
          <p className="text-gray-600 mt-2">{ title }</p>

          
      </div>
  );
}

export default LinksCard;