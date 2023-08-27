function Card({ title, content, imageUrl }) {
  return (
      <div className="card bg-white p-4 rounded-md shadow-md my-4">
          {imageUrl && <img src={imageUrl} alt={title} className="w-full h-48 object-cover rounded-md" />}
          <h2 className="text-xl font-bold mt-4">{title}</h2>
          <p className="text-gray-600 mt-2">{content}</p>
      </div>
  );
}

export default Card;