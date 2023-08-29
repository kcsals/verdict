// LinksCard.jsx

function LinksCard({ spotLight, titles = [] }) {
  return (
    <div className="card bg-white p-4 rounded-md shadow-md my-4 cursor-pointer">
      <h3>{spotLight}</h3>
      <hr className="my-4 border-t border-gray-300" />
      <ul>
        {titles.map((title, index) => (
          <li key={index} className="text-gray-600 mt-2">{title}</li>
        ))}
      </ul>
    </div>
  );
}

export default LinksCard;